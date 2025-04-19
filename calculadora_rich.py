from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box

console = Console()

def calculate(expression: str):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except Exception as e:
        return f"[red]Erro:[/red] {str(e)}"

def show_calculator():
    console.clear()
    console.rule("[bold green]🧮 Calculadora Terminal Estilizada")
    
    while True:
        console.print(Panel("Digite a operação (ex: [bold cyan]2 + 3 * 5[/bold cyan]) ou [bold red]'sair'[/bold red] para encerrar.",
                            box=box.ROUNDED, style="blue"))
        
        expr = Prompt.ask("[bold yellow]Informe a expressão[/bold yellow]")
        
        if expr.lower() in ["sair", "exit", "q"]:
            console.print("\n[bold green]Obrigado por usar a calculadora! Até mais! 👋[/bold green]")
            break
        
        result = calculate(expr)
        console.print(Panel(f"Resultado: [bold green]{result}[/bold green]", style="magenta", box=box.DOUBLE))

if __name__ == "__main__":
    show_calculator()
