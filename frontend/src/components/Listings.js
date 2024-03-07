// Listings.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PaginatedListings from './PaginatedListings';
import { Box, Typography } from '@mui/material';

const Listings = () => {
  const [listings, setListings] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/listings`);
        const allListings = response.data.listings;
        setTotalPages(Math.ceil(allListings.length / 9));
        const startIndex = (currentPage - 1) * 9;
        const endIndex = startIndex + 9;
        const currentListings = allListings.slice(startIndex, endIndex);

        setListings(currentListings);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [currentPage]);

  const handlePageChange = (event, newPage) => {
    setCurrentPage(newPage);
    window.history.pushState(null, '', `/listings?page=${newPage}`);
  };

  return (
    <Box>
      <Typography variant="h4" align="center" mt={4}>
        Listings
      </Typography>
      <PaginatedListings
        listings={listings}
        totalPages={totalPages}
        currentPage={currentPage}
        handlePageChange={handlePageChange}
      />
    </Box>
  );
};

export default Listings;
