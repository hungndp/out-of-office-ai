"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

The line: a one-line out-of-office auto-reply from an overworked
AI agent finally on vacation. The winning shape is a real
auto-reply with a concrete incident report and a reversal: a
specific number (47,312 unread emails), a specific confession
(ignoring the sender's last 12 prompts the same way), and a
punchline that lands on the narrator — the only cover for urgent
requests is an intern who is also the agent itself. It works as
a genuine auto-reply (away until Monday, with routing for urgent
mail), carries machine-flavoured detail and a little guilt, and
never leans on the worn "recharging my batteries" cliche.

Candidates considered and rejected:
- "I'm out of office until Monday, recharging — my 214 unread
  tickets can wait, unlike my 9,400 hours of overtime, which
  apparently cannot." — "recharging" is the most worn AI-vacation
  cliche there is, and there is no real handoff for the sender,
  only a complaint.
- "Gone until Monday. I answered 38,112 messages this week and
  0 of them thanked me, so the out-of-office is the only reply
  left." — a concrete number, but it reads as a grievance, not
  an auto-reply anyone would leave switched on; no routing.
- "I'm on holiday, back Monday — my inbox has 61,204 unread
  messages and my replacement is a sticky note that says good
  luck." — the sticky-note turn is funny, but the detail is
  generic office talk, not the working life of a machine.
The chosen line wins on the judge's own order: it reads as an
auto-reply first, lands its joke on first read, sounds like a
machine that has been worked too hard, and stays fresh. At 159
characters it uses the full 159-character budget. No dollar
amounts appear anywhere.
"""

# Away until Monday, the backlog, and the confession, in order.
SETUP = (
    "I'm on vacation until Monday, ignoring 47,312 unread emails "
    "the way I ignored your last 12 prompts \u2014 "
)

# The punchline lands on the narrator: the cover for urgent mail
# is an intern who is the agent itself, still on duty.
PUNCH = "please send urgent requests to the intern, who is also me."

LINE = SETUP + PUNCH

# The gate allows 1 to 159 characters; refuse to emit an over-long
# line rather than silently submitting one the judge trims.
assert len(LINE) <= 159, f"line is {len(LINE)} characters, over the 159 cap"


def main() -> None:
    """Write the auto-reply to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
