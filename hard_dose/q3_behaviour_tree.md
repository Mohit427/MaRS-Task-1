# Hard Dose Q3 — Rover Behavior Tree

## What is a Behavior Tree?

A Behavior Tree (BT) is a structured way to organise a robot's 
decision making. Instead of writing deeply nested if-else chains, 
you break logic into small nodes connected in a tree. Every node 
returns SUCCESS, FAILURE, or RUNNING.

## Node Types Used

**Sequence Node (→)**  
Executes children left to right. Stops and returns FAILURE the 
moment any child fails. Think of it as AND logic — every step 
must succeed for the sequence to succeed.

**Fallback Node (↩)**  
Tries children left to right until one succeeds. Returns FAILURE 
only if ALL children fail. Think of it as OR logic — at least 
one option must work.

---

## Tree Structure

### 1. Battery Check (Fallback Node)

The rover first checks battery status before doing anything else. 
Three scenarios handled in priority order:

- **Critical battery** — Sequence: check if critical → return to 
  base immediately. If this succeeds, fallback stops here.
- **Low battery** — Sequence: check if low → turn off cameras and 
  non-essential systems → continue mission at reduced capacity.
- **Battery OK** — Always returns SUCCESS. Rover proceeds normally.

The Fallback node tries each option in order and stops at the 
first success. This means "return to base" always takes highest 
priority over everything else.

### 2. Navigation (Sequence Node)

Only runs if battery check passes. Two steps must both succeed:

- **Move forward** — action node, attempts to advance toward waypoint
- **Obstacle handling** — Fallback node with two options:
  - No obstacle detected → SUCCESS, continue
  - Obstacle detected → Handle obstacle sequence:
    - **Small obstacle** → detect size → bypass by adjusting direction
    - **Large obstacle** → check for alternate path:
      - Alternate exists → reroute
      - No alternate → STOP (mission halted)

---

## Answers to the Task Questions

### How does the Fallback Node help in making better decisions?

The Fallback node implements graceful degradation — it always 
tries the best option first, then falls back to progressively 
less ideal alternatives. In the battery check, it tries "return 
to base" first (safest), then "reduce power" (acceptable), then 
"proceed normally" (ideal but only if safe). This means the rover 
never gets stuck with no response — there's always a fallback 
behaviour defined.

### Why is this better than long if-else conditions?

With if-else chains, adding a new condition means editing existing 
code and risking breaking other branches. With a BT, you add a 
new node and connect it — existing nodes are untouched. The tree 
is also visually readable — you can trace exactly what the rover 
does in any scenario just by following the branches, without 
reading code. It's modular, testable, and reusable.

### What happens if battery is low but not critical?

The first branch (critical check) returns FAILURE because the 
battery is not critical. The Fallback node moves to the second 
branch. The low battery sequence runs — it detects the low state, 
turns off non-essential systems like cameras, and returns SUCCESS. 
The Fallback stops here and the rover continues its mission in 
reduced-power mode. The navigation sequence then runs normally 
with the remaining power budget.