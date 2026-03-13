import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ProfilePage.css';

const ProfilePage: React.FC = () => {           //component called ProfilePage function
    const navigate = useNavigate();

    return (
        <div className = "profile-page">
            <div className = "profile-container">
                <h1>Your Profile</h1>

                <div className = "profile-info">
                    <div className = "info-email">
                        <label>Email:</label>
                        <p>{}</p>
                    </div>

                    <div className = "info-name">
                        <label>Name:</label>
                        <p>{}</p>
                    </div>
                </div>

                <button className = "back-btn" onClick = {() => navigate('/')}>
                    Back To Home
                </button>
            </div>
        </div>
    );
};

export default ProfilePage;