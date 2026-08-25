from mahou.core.app import App
import sys


def execute():
    print("Running!")
    try:
        app = App()
        app.run()
    finally:
        print("Ended.")

if __name__ == "__main__":
    
    sys.exit(execute())
    