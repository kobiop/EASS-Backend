// ListingCard.jsx
import React from 'react';
import { Card, CardContent, Grid, Typography } from '@mui/material';

const ListingCard = ({ listing }) => {
    return (
        <Card style={{ marginBottom: '16px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
            <CardContent>
                <Typography variant="h6" style={{ marginBottom: '8px' }}>{listing.address}</Typography>
                <Grid container spacing={2}>
                    <Grid item xs={6}>
                        <Typography variant="body2">Price: ${listing.price}</Typography>
                        <Typography variant="body2">Year Built: {listing.year_built}</Typography>
                        <Typography variant="body2">SQFT: {listing.sqft}</Typography>
                        <Typography variant="body2">SQFT Lot: {listing.sqft_lot}</Typography>
                        <Typography variant="body2">Price per SQFT: ${listing.price_per_sqft}</Typography>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography variant="body2">Bathrooms: {listing.bathrooms}</Typography>
                        <Typography variant="body2">Beds: {listing.beds}</Typography>
                        <Typography variant="body2">Property Type: {listing.property_type}</Typography>
                        <Typography variant="body2">Garage: {listing.garage}</Typography>
                        <Typography variant="body2">HOA Fees: ${listing.HOA_fees}</Typography>
                    </Grid>
                </Grid>
            </CardContent>
        </Card>
    );
};

export default ListingCard;