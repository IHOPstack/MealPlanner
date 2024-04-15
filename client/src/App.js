import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Recipes from './pages/Recipes';
import MealPlans from './pages/MealPlans';
import GroceryLists from './pages/GroceryLists';

const App = () => {
  return (
    <Provider store={store}>
      <Router>
        <div>
          <Navbar />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/recipes" component={Recipes} />
            <Route path="/meal-plans" component={MealPlans} />
            <Route path="/grocery-lists" component={GroceryLists} />
          </Switch>
        </div>
      </Router>
    </Provider>
  );
};

export default App;
