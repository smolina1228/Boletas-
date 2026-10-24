import os
import re
import requests

# URL de la boletería individual para el clásico
URL = "https://www.tribunaverde.com/event/an-vs-dim--liga-betplay-dimayor-2026-ii-boleteria-individual"

# Token y Chat ID definidos directamente
TELEGRAM_TOKEN = "8851647339:AAHriVerlci0MvZcJ-ugtFaPa6bPVwwuNIk"
CHAT_ID = "983154068"


def check_tickets():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
    }
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        html_text = response.text

        # Verificamos si la palabra "agotado" (en minúsculas/mayúsculas) sigue estando en la página
        esta_agotado = "agotado" in html_text.lower()

        if not esta_agotado:
            # Solo si la palabra "agotado" desaparece por completo, envía la alerta real
            message = (
                "🚨 ¡ALERTA BOLETAS DISPONIBLES! 🚨\n\nSe detectó disponibilidad para"
                f" el clásico Nacional vs. DIM.\n\nCompra aquí: {URL}"
            )
            telegram_url = (
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            )
            res = requests.post(telegram_url, data={"chat_id": CHAT_ID, "text": message})
            
            if res.status_code == 200:
                print("¡Alerta real enviada a Telegram con éxito!")
            else:
                print(f"❌ Error de Telegram ({res.status_code}): {res.text}")
        else:
            print("Sigue agotado en Tribuna Verde. No se envía alerta.")
            
    except Exception as e:
        print(f"Error al verificar la página: {e}")


if __name__ == "__main__":
    check_tickets()
