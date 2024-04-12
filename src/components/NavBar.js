import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/joy';

const Navbar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Meal Planner
        </Typography>
        <Button component={Link} to="/" color="inherit">Home</Button>
        <Button component={Link} to="/recipes" color="inherit">Recipes</Button>
        <Button component={Link} to="/meal-plans" color="inherit">Meal Plans</Button>
        <Button component={Link} to="/grocery-lists" color="inherit">Grocery Lists</Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
