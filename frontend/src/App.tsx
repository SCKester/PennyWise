import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import ProfilePage from './pages/ProfilePage';
import BudgetCreation from './pages/BudgetCreation';
import './App.css';
import CreateWeekly from './pages/CreateWeekly';
import CreateMonthly from './pages/CreateMonthly';
import CreateYearly from './pages/CreateYearly';
import LoginPage from './pages/LoginPage';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element={<MainPage />} />
        <Route path = "profile" element={<ProfilePage />} />
        <Route path = "budget" element={<BudgetCreation />} />
        <Route path = "week-budg" element={<CreateWeekly />} />
        <Route path = "month-budg" element={<CreateMonthly/>} />
        <Route path = "year-budg" element={<CreateYearly/>} />
        <Route path = "login" element={<LoginPage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
