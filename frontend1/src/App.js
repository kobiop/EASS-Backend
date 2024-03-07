import React from 'react';
import Listings from './components/Listings';
import Navbar from './components/Navbar'
import UserPreferencesForm from './components/SearchForm';
import AddNewListing from './components/AddNewListing'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Box } from '@mui/material';

function App() {
  return (
    <Box>
      <Router>
        < Navbar />
        <Routes>
          <Route path='/' element={<Listings />} />
          <Route path='/listings' element={<Listings />} />
          <Route path='/Search' element={<UserPreferencesForm />} />
          <Route path='/addnew' element={<AddNewListing />} />
        </Routes>
      </Router>
    </Box>
  );
}

export default App;
