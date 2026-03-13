import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import './CreateYearly.css';

const CreateYearly: React.FC = () => {
  const navigate = useNavigate();
  const [income, setIncome] = useState<number | ''>('');
  const [categories, setCategories] = useState([{name: '', amount: ''}]);

  //calculating totals
  const totalSpent = categories.reduce((sum, c) => sum + (Number(c.amount) || 0), 0);
  const leftOver = (Number(income) || 0) - totalSpent;

  const handleCategoryChange = (index: number, field: string, value: string) => {
    const updated = [...categories];
    (updated as any)[index][field] = value;
    setCategories(updated);
  };

  const addCategory = () => {
    setCategories([...categories, {name: '', amount: ''}]);
  };

  const removeCategory = (index: number) => {
    const updated = categories.filter((_, i) => i !== index);
    setCategories(updated)
  };


  return (
    <div className="create-yearly">
      <h1>Create a budget for the year!</h1>

    <div className='budget-square'>
      <div className="income-entry">
        <label className="income-label">Yearly Income/Amount: </label>
        <input
          type="number"
          value={income}
          onChange={(e) => {
            const value = e.target.value;
            const numericValue = parseFloat(value);
            setIncome(value === '' ? '': isNaN(numericValue) ? 0 : numericValue);
          }}
          placeholder="Enter income"
        />
      </div>

        <div className = "budget-entry-section">
          <div className='budget-entry-labels'>
            <label className='category-label'>Category </label>
            <label className='amount-label'>Amount</label>
          </div>

          {categories.map((cat, index) => (
            <div key={index} className="budget-row">
              <input
                type="text"
                placeholder="Category name"
                value={cat.name}
                onChange={(e) => handleCategoryChange(index, 'name', e.target.value)}
              />
              <input
                type="number"
                placeholder="Amount"
                value={cat.amount}
                onChange={(e) => handleCategoryChange(index, 'amount', e.target.value)}
              />
              <button className="remove-btn" onClick={() => removeCategory(index)}>
                x
              </button>
            </div>
          ))}

          <button className="add-btn" onClick={addCategory}>
            + Add Category
          </button>
        </div>

      <div className='totals'>
        <div>
          <label className='spent'>Total Spent </label>
          <span>${totalSpent.toFixed(2)}</span>
        </div>

        <div>
          <label className='excess'>Left Over</label>
          <span>${leftOver.toFixed(2)}</span>
        </div>
      </div>
    </div>
      
    </div>
  );
};

export default CreateYearly;
