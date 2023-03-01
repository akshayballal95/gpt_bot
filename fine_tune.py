import openai
import subprocess

subprocess.run('openai tools fine_tunes.prepare_data --file fine_tune.csv --quiet'.split())
