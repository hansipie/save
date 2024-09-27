import typer
import sys
import os

from typing_extensions import Annotated


def main(
    filename: Annotated[str, typer.Argument(help="Filename without extension.")],
    ext: Annotated[str, typer.Option(help="Custom file extension.")] = "txt",
    silent: Annotated[
        bool, typer.Option(help="Don't use STDOUT for output, only save to the file.")
    ] = False,
):
    """
    save: a "tee-like" utility to pipeline saving of content, while keeping the output stream intact.
    """
    path = os.environ.get("SAVE_OUTPUT_PATH")
    if not path:
        typer.secho(
            "Error: Environment variable 'SAVE_OUTPUT_PATH' not set.", err=True
        )
        raise typer.Exit(1)
    output = os.path.join(path, f"{filename}.{ext}")

    with open(output, "w") as file:
        try:
            while True:
                input_line = sys.stdin.readline()
                if not input_line:
                    break  # EOF
                # write to file
                file.write(input_line)
                # write to stdout if not silent
                if not silent:
                    sys.stdout.write(input_line)
                    sys.stdout.flush()  # Ensure the output is written immediately
                
        except KeyboardInterrupt:
            pass  # Handle any cleanup here if necessary
        

if __name__ == "__main__":
    typer.run(main)
