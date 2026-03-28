# vim

## Common commands


| Command        | Action                              |
| -------------- | ----------------------------------- |
| gg             | Go to top of file                   |
| G              | Go to bottom of file                |
| :N             | Jump to line N (e.g., `:15`)        |
| V              | Start selecting lines (Visual Line) |
| d              | Delete selection                    |
| dd             | Delete a single line                |
| u              | Undo (lifesaver)                    |
| i              | Enter Insert mode (to type)         |
| Esc            | Back to Normal mode                 |
| :wq            | Save and quit                       |
| :q!            | Quit without saving                 |
| vim myfile.txt | Open file                           |
| Cmd+V          | Workflow Step 7: Paste content      |
| Esc            | Workflow Step 8: Exit Insert mode   |
| :wq            | Workflow Step 9: Save and exit      |


## Workflow to delete line x to line y


| Command | Workflow step                              |
| ------- | ------------------------------------------ |
| :10     | Workflow Step 2: Jump to line 10           |
| V       | Workflow Step 3: Start selecting           |
| :50     | Workflow Step 4: Highlight through line 50 |
| d       | Workflow Step 5: Delete the block          |
| i       | Workflow Step 6: Enter Insert mode         |


## Word and line movements


| Command  | Action                                                                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------------------------ |
| w        | Move right (start of next word) / Jump to the start of the next **w**ord.                                                |
| b        | Move left / Jump **b**ack to the start of the previous word.                                                             |
| e        | Jump to the **e**nd of the word.                                                                                         |
| 0 (zero) | Jump to the beginning of the line.                                                                                       |
| $        | Jump to the end of the line.                                                                                             |
| %        | Jump between matching brackets `()`, `[]`, or `{}`. This is a lifesaver for finding the end of a function or "if" block. |


## Copying stuff


| Command | Action                                                                         |
| ------- | ------------------------------------------------------------------------------ |
| :%y+    | Breakdown: `%` selects entire file, `y` yanks, `+` copies to system clipboard. |


## Line movements


| Command | Action              |
| ------- | ------------------- |
| 10j     | Move 10 lines below |
| 10k     | Move 10 lines above |


## Basic movement keys


| Key | Direction |
| --- | --------- |
| h   | left      |
| j   | down      |
| k   | up        |
| l   | right     |


## Other helpful commands 

- Add `set number` and `set relativenumber` to show line numbers. 
- Add `set autoindent` to auto indent the code. 

