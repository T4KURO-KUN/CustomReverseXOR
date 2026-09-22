import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def chiffrer(texte: str, cle: int = 0x42) -> str:
    """Chiffre une chaîne de caractères par XOR et inversion."""
    hex_list = [f"{ord(c) ^ cle:02x}" for c in texte[::-1]]
    return "0x" + "".join(hex_list)

def dechiffrer(code_hex: str, cle: int = 0x42) -> str:
    """Déchiffre un code hexadécimal généré par la fonction chiffrer."""
    clean_hex = code_hex.removeprefix("0x")
    chars_inv = [chr(int(clean_hex[i:i+2], 16) ^ cle) for i in range(0, len(clean_hex), 2)]
    return "".join(chars_inv)[::-1]

def main() -> None:
    try:
        while True:
            console.clear()  # Nettoie l'écran proprement
            console.print(Panel.fit("[bold cyan]Custom Reverse XOR[/bold cyan]\n[dim]CLI Encryption Tool[/dim]", border_style="blue"))
            
            console.print("[1] Encrypt a message")
            console.print("[2] Decrypt a message")
            console.print("[3] Exit\n")
            
            choix = console.input("[bold green]Choice (1-3) : [/]").strip()

            if choix == "1":
                msg = console.input("[bold green]Text to encrypt : [/]").strip()
                resultat = chiffrer(msg)
                console.print(f"\n[bold]Result :[/bold] [cyan]{resultat}[/cyan]")

            elif choix == "2":
                code = console.input("[bold green]Hex code to decrypt : [/]").strip()
                try:
                    resultat = dechiffrer(code)
                    console.print(f"\n[bold]Result :[/bold] [cyan]{resultat}[/cyan]")
                except (ValueError, IndexError):
                    console.print("[bold red]Error : Invalid hexadecimal format.[/bold red]\n")

            elif choix == "3":
                console.print("[dim]Exiting...[/dim]")
                sys.exit(0)

            else:
                console.print("[bold red]Error : Invalid option.[/bold red]\n")

            console.input("[dim]Press Enter to return to main menu...[/dim]\n")
            
    except KeyboardInterrupt:
        console.print("\n[dim]Exiting...[/dim]")
        sys.exit(0)

if __name__ == "__main__":
    main()