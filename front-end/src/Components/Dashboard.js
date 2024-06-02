// src/components/Dashboard.js

import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import '../Css/Dashboard.css';
import template1 from '../Images/Template1.png'
import template2 from '../Images/Template2.png'
import template3 from '../Images/Template3.png'


const Dashboard = () => {
  return (
    <div>
      <header className="header-nav">
        <h1>General Magic</h1>
      </header>
      <nav className="dashboard-nav">
        <ul>
          <li><Link to="/dashboard">Home</Link></li>
          <li><Link to="/user-details">User Details</Link></li>
          <li><Link to="/logout">Logout</Link></li>
        </ul>
      </nav>
      <div className="dashboard-content">
            <div className="image-row">
                <div className="image-block">
                <img src={template1} alt="Placeholder 1" />
                <p>Template 1</p>
                </div>
                <div className="image-block">
                <img src={template2} alt="Placeholder 2" />
                <p>Template 2</p>
                </div>
                <div className="image-block">
                <img src={template3} alt="Placeholder 3" />
                <p>Template 3</p>
                </div>
            </div>
            <Outlet/>
      </div>
    </div>
  );
};

export default Dashboard;
