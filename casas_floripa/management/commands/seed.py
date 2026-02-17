import glob
import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Roda todos os seeds na ordem (seeds/0010_*, 0020_*, ...)"

    def handle(self, *args, **options):
        seeds_dir = os.path.join(os.getcwd(), "seeds")
        scripts = sorted(glob.glob(os.path.join(seeds_dir, "[0-9]*_seed_*.py")))

        if not scripts:
            self.stderr.write("Nenhum seed encontrado em seeds/")
            return

        for script in scripts:
            nome = os.path.basename(script)
            self.stdout.write(f"\n{'=' * 60}")
            self.stdout.write(f"Rodando {nome}...")
            self.stdout.write("=" * 60)
            with open(script) as f:
                exec(f.read(), {"__name__": "__main__"})

        self.stdout.write(self.style.SUCCESS(f"\nTodos os {len(scripts)} seeds concluídos!"))
