import Header from "../components/Header.jsx";
import Recipe from "../components/Recipe.jsx";

function RecipesPage() {
  return (
    <div>
      <Header />
      <h2 className="title">Recipes</h2>
      <div className="recipe-list">
        <Recipe />
        <Recipe />
        <Recipe />
      </div>
    </div>
  );
}

export default RecipesPage;
