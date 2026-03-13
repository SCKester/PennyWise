import React from 'react';
import { useNavigate } from 'react-router-dom'; // function to get to different pages V
import './MainPage.css';
import './BudgetCreation.css';
import './CreateWeekly.css';

const MainPage: React.FC = () => {              // component called MainPage function
    const navigate = useNavigate();             //the function in question

    return (
        <div className = "main-page">
            <header>
                <h1> PennyWise </h1>
                <p>Your Smart Budgeting App </p>
            </header>

            <div className = "main-content">
            <h2>Welcome to PennyWise!</h2>
            <p>Track your expenses, manage your budget, and reach your financial goals.</p>

            <div className="button-group">
                <button className = "primary-btn" onClick={() => navigate('/profile')}>
                    View Profile
                </button>

                <button className = "budget-btn" onClick={() => navigate('/budget')}>
                    Create Budget
                </button>
            </div>
            </div>
        </div>
    );
};

export default MainPage;
