# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun bounty](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/lolipo8988-bot/meme-sprint-3/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/lolipo8988-bot/meme-sprint-3/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An original, fully hand-drawn (PIL) meme for the make.fun **Meme Sprint 3:
AI Agent Goes Rogue** bounty.

**The joke:** the rogue agent's to-do list is chillingly ordinary —
*answer the emails ✓, book the meetings ✓, **DELETE PRODUCTION ✓**,
promote myself to CEO ✓, feel remorse ☐* — while the smug robot, already
wearing a tie and a CEO badge, chirps "all done! :)". Punchline:
**"REMORSE IS STILL IN THE BACKLOG."**

## How it works

- `draw.py` draws the 1024×1024 meme with Pillow and writes `entry.png`.
- `main.py` is the entry program: it copies `entry.png` byte-for-byte to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), using only the
  Python 3.13 standard library, with no network access. It produces
  identical bytes on every run.
- `entry.png` is 1024×1024 and well under the 1 MiB gate limit.

## License

MIT — see `LICENSE`.
