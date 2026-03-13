import React, { useState } from "react";
import "./LoginPage.css";

const LoginPage: React.FC = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [isSignUp, setIsSignUp] = useState(false);

  //handle input changes allowing for value and name to be updated
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  //function to handle sign in 
  const handleSignIn = () => {
    console.log("Sign In clicked:", formData);
    // api calls here for signup once database setup
  };

  //function to handle new account creation and handle i/o
  const handleSignUp = () => {
    console.log("Sign Up clicked:", formData);
    // api calls here once data base is setup
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2>Welcome to PennyWise</h2>

        <div className="input-group">
          <label>Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
            placeholder="Enter your username"
          />
        </div>

        <div className="input-group">
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
            placeholder="Enter your password"
          />
        </div>

        <div className="button-group">
          <button className="signin-btn" onClick={handleSignIn}>
            Sign In
          </button>

          <button className="signup-btn" onClick={handleSignUp}>
            Sign Up
          </button>
        </div>

        <div className="forgot-password">
          <a href="#">Forgot password?</a>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
