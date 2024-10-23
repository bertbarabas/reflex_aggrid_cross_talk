# Test case for reflex issue with cross talk between two AgGrid components

Steps to reproduce issue:

1. Install and run this reflex program
2. In the browser click on a column in Grid1
3. Notice that the correct message is displayed below the grid
4. Switch to Grid2 using the drop down (message is cleared)
5. Notice that although there is no on_cell_clicked function defined for grid2, we still get the message printed when we click on a cell!
6. Uncomment the on_cell_clicked line for grid2
7. Notice that now that each grid has an on_cell_clicked function provided, that it does call the correct one.