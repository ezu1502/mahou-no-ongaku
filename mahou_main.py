from mahou.core.master import Master
from mahou_libs.bocca.bocca_setup import get_master
from mahou_libs.bocca.bocca_main import BoccaFiglia
import sys

main_logger = get_master()
log = BoccaFiglia("main", "#FFAA00")

def execute():
    master = Master()
    master.run()

if __name__ == "__main__":
    sys.exit(execute())