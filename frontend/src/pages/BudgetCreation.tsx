import React from 'react';
import { useNavigate } from 'react-router-dom'; // function to get to different pages V
import './BudgetCreation.css';

const BudgetCreation: React.FC = () => {              // component called MainPage function
    const navigate = useNavigate();             //the function in question

    return (
        <div className = "budget-creation">
            <header>
                <h1> Your Budget </h1>
                <p> </p>
            </header>

            <div className = "budget-instruc">
                <h2>Budget Creation</h2>
                <p>Create a budget for the week, month, or year.</p>
            </div>
            
            <div className = "budget-containers">

                <div className = "month">      
                    <h2>Weekly Budget</h2>
                    <p>Create a small budget for the week!</p>

                    <div className = "budget-btns">
                        <button className = "week-btn" onClick={() => navigate('/week-budg')}>
                            Create Weekly Budget
                        </button>
                    </div>
                </div>

                <div className = "month">
                    <h2>Monthly Budget</h2>
                    <p>Create a budget for your monthly income and expenses!</p>

                    <div className = "budget-btns">
                        <button className = "month-btn" onClick={() => navigate('/month-budg')}>
                            Create Monthly Budget
                        </button>
                    </div>
                </div>

                <div className = "year">
                    <h2>Yearly Budget</h2>
                    <p>Create a budget for your yearly goals!</p>

                    <div className = "budget-btns">
                        <button className = "year-btn" onClick={() => navigate('/year-budg')}>
                            Create Yearly Budget
                        </button>
                    </div>
                </div>

            </div>

            
        </div>
    );
};

export default BudgetCreation;