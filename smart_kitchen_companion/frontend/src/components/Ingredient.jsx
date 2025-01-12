import React, { useState } from "react";
import "../styles/IngredientList.css";

const IngredientList = () => {
  const [ingredients, setIngredients] = useState([]);
  const [newIngredient, setNewIngredient] = useState({
    name: "",
    quantity: "",
    expiry: "",
  });
  const [showAddForm, setShowAddForm] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewIngredient({ ...newIngredient, [name]: value });
  };

  const addIngredient = () => {
    setIngredients([...ingredients, newIngredient]);
    setNewIngredient({ name: "", quantity: "", expiry: "" });
    setShowAddForm(false);
  };

  const removeIngredient = (index) => {
    const newIngredients = ingredients.filter((_, i) => i !== index);
    setIngredients(newIngredients);
  };

  return (
    <div className="ingredient-list-container">
      <h2>Ingredients</h2>
      <ul>
        {ingredients.map((ingredient, index) => (
          <li key={index} className="ingredient-item">
            <span>
              {ingredient.name} - {ingredient.quantity} - {ingredient.expiry}
            </span>
            <div className="actions">
              <button onClick={() => removeIngredient(index)}>Remove</button>
            </div>
          </li>
        ))}
      </ul>
      <button onClick={() => setShowAddForm(true)} className="add-ingredient">
        Add Ingredient
      </button>
      {showAddForm && (
        <div className="add-form">
          <input
            type="text"
            name="name"
            placeholder="Name"
            value={newIngredient.name}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="quantity"
            placeholder="Quantity"
            value={newIngredient.quantity}
            onChange={handleInputChange}
          />
          <input
            type="date"
            name="expiry"
            placeholder="Expiry Date"
            value={newIngredient.expiry}
            onChange={handleInputChange}
          />
          <button onClick={addIngredient}>Submit</button>
        </div>
      )}
    </div>
  );
};

export default IngredientList;
