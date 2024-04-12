import React from 'react';
import { useSelector } from 'react-redux';
import { List, ListItem, ListItemText, Checkbox } from '@mui/joy';

const GroceryLists = () => {
  const groceryLists = useSelector((state) => state.groceryLists);

  return (
    <div>
      <h2>Grocery Lists</h2>
      <List>
        {groceryLists.map((groceryList) => (
          <ListItem key={groceryList.id}>
            <ListItemText primary={groceryList.name} />
            <List>
              {groceryList.items.map((item) => (
                <ListItem key={item.id}>
                  <Checkbox checked={item.checked} />
                  <ListItemText primary={item.ingredient.name} secondary={`${item.amount} ${item.unit}`} />
                </ListItem>
              ))}
            </List>
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default GroceryLists;
