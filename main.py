"""Entry for make.fun bounty u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.

Writes one single-line review of planet Earth, left by an alien
tourist after two days of observation, to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The review: a field note about the locals queuing for bitter bean
water, paying extra to have their names spelled wrong on the cup,
and calling it a morning ritual — with a tourist's rating at the
end. 149 characters, one line, inside the 1-200 gate. The angle
stays clear of the obvious topics (traffic, gravity, money,
weather) and lands its single joke at the end.
"""

import os

LINE = (
    "Field note, day 2: the locals queue for bitter bean water, "
    "pay extra to have their names spelled wrong on the cup, "
    "and call it a morning ritual. 4/5."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
