import { useState } from "react";
import "../styles/InsertFile.css";

function InsertFile() {
  const [receipt, setReceipt] = useState(null);
  const [groceries, setGroceries] = useState(null);

  const handleReceiptChange = (event) => {
    setReceipt(event.target.files[0]);
  };

  const handleGroceriesChange = (event) => {
    setGroceries(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle the form submission logic here
    console.log("Receipt:", receipt);
    console.log("Groceries:", groceries);
  };

  return (
    <form onSubmit={handleSubmit} className="insert-file-form">
      <div>
        <label htmlFor="receipt">Add Receipt:</label>
        <input
          type="file"
          id="receipt"
          accept="image/*"
          onChange={handleReceiptChange}
        />
      </div>
      <div>
        <label htmlFor="groceries">Add Photo of Groceries:</label>
        <input
          type="file"
          id="groceries"
          accept="image/*"
          onChange={handleGroceriesChange}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

export default InsertFile;
