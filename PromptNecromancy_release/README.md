# PromptNecromancy

Category: Misc

Difficulty: Insane

So you people really cannot solve anything anymore without shoving it into some overgrown autocomplete and praying it hallucinates competence for you. Pathetic. If your first instinct in a CTF is to beg a silicon fortune cookie to think for you, then this challenge was built to laugh in your face.

What you have here is a local oracle from the same rotten cult of benchmark addicts, prompt beggars, and clipboard necromancers who keep pretending that pasting artifacts into an AI counts as technical skill. It speaks just enough to keep idiots busy. It hides what matters. It also seems to trust the wrong things for the wrong reasons, which is exactly the kind of stupid design people like you deserve.

No extra files. No remote service. No excuses. If you want the answer, stop roleplaying as a prompt engineer and actually tear the thing apart.

Files:
- `oracle.py`
- `run.sh`
- `run.bat`

Run it, genius:

```bash
chmod +x run.sh
./run.sh
```

Then pick a room id and type your trash prompt when it asks.

Or if touching the interactive wrapper is somehow too advanced for you:

```bash
python3 oracle.py "your trash query here"
```

On Windows, try not to embarrass yourself:

```bat
run.bat
```
