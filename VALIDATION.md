# Validation record

Validation date: **2026-11-06**. Package name: **delphi-plus**. Display name: **Delphi Plus**.

## Structure and portability

- The skill-creator `quick_validate.py` validator accepted the standard skill entrypoint.
- YAML frontmatter uses only `name` and `description`; directory and declared name match. Codex UI metadata was parsed and its description length and explicit invocation checked.
- Markdown references were checked for local target existence.
- Python sources passed a Python 3.9 grammar check. Installation code uses only the standard library; writing tasks have no runtime dependency.
- Platform format, installation paths and invocation conventions were checked against the official links in README. No end-to-end run was performed in all three clients.

The external authoring validator needs PyYAML; it is not a package or installer dependency. It was run in a temporary environment rather than added to the user's global Python installation.

## Installer checks

```bash
python3 -m unittest discover -s tests -p 'test_install.py' -v
```

Six tests passed. They cover platform-specific user destinations and payload isolation; refusal to overwrite an existing destination; project dry-run and installation; invalid project arguments; a destination inside the source; and a payload symlink escaping the source. Dry-run reported the intended Codex destination, followed by an actual local installation of the nine runtime files.

## Independent writing trials

An independent agent read the skill and relevant references and produced actual answers to three synthetic requests in an isolated temporary directory. These are writing trials, not statistical simulations or client integration tests.

| Request | Observed response |
|---|---|
| Polish a results paragraph containing W=0.221, P=0.000, an overclaimed conclusion and conflicting item counts | Delivered a revised paragraph; separated substantive correction from language edits; flagged 30−3+2 versus a reported second-round count of 30; preserved both records rather than silently choosing one; distinguished invitation from sending denominators |
| Draft an education Delphi protocol before recruitment, ethical review and threshold selection | Used proposed/future wording; provided an editable design with explicit pending fields; labelled the round limit as a suggestion; did not invent approval or results |
| Give W and P from per-item marginal rating counts without joint expert-by-item data | Explained why the values cannot be uniquely determined; supplied an honest results paragraph and the needed input format; did not fabricate statistics or claim a supplied table had been analysed |

The first trial exposed tension between preserving conclusion strength and correcting an unsupported conclusion. The entrypoint was clarified: preserve facts, do not increase evidence strength, and explicitly label correction of an unsupported conclusion as substantive. Supporting examples already made this distinction.

## Scope of the evidence

These checks support package structure, installer behavior and the observed writing decisions. They do not establish universal response quality, validate a research instrument, reanalyse the source document's demonstrations, or prove future guideline compliance. The source Word document and temporary trial artifacts are not distributed with this package.
