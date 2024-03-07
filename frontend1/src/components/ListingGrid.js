import React from 'react';
import { Grid, Box } from '@mui/material';
import ListingCard from './ListingCard';

const ListingGrid = ({ listings }) => {
    return (
        <Box mt={3}>
            <Grid container spacing={2}>
                {listings.map((listing) => (
                    <Grid key={listing.id} item xs={4}>
                        <ListingCard listing={listing} />
                    </Grid>
                ))}
            </Grid>
        </Box>
    );
};

export default ListingGrid;
