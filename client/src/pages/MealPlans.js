import React from 'react';
import { useSelector } from 'react-redux';
import { List, ListItem, ListItemText } from '@mui/joy';

const MealPlans = () => {
  const mealPlans = useSelector((state) => state.mealPlans);

  return (
    <div>
      <h2>Meal Plans</h2>
      <List>
        {mealPlans.map((mealPlan) => (
          <ListItem key={mealPlan.id}>
            <ListItemText primary={mealPlan.name} secondary={`${mealPlan.startDate} - ${mealPlan.endDate}`} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default MealPlans;