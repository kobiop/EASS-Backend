// PaginatedListings.jsx
import React from 'react';
import { Grid, Box, Pagination } from '@mui/material';
import ListingCard from './ListingCard';

const PaginatedListings = ({ listings, totalPages, currentPage, handlePageChange }) => {
    return (
        <>
            <Grid container spacing={2}>
                {listings.map((listing) => (
                    <Grid key={listing.id} item xs={4}>
                        <ListingCard listing={listing} />
                    </Grid>
                ))}
            </Grid>
            <Box display="flex" justifyContent="center" mt={3}>
                <Pagination
                    count={totalPages}
                    page={currentPage}
                    onChange={handlePageChange}
                    color="primary"
                    style={{ marginTop: '20px' }}
                />
            </Box>
        </>
    );
};

export default PaginatedListings;
