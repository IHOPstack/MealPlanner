import React from 'react';
import { useSelector } from 'react-redux';
import { List, ListItem, ListItemText } from '@mui/joy';

const Recipes = () => {
  const recipes = useSelector((state) => state.recipes);

  return (
    <div>
      <h2>Recipes</h2>
      <List>
        {recipes.map((recipe) => (
          <ListItem key={recipe.id}>
            <ListItemText primary={recipe.name} secondary={recipe.description} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default Recipes;
