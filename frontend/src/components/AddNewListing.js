import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Grid, Typography, TextField, InputLabel, Select, MenuItem, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const NewListingForm = () => {
    const [newListing, setNewListing] = useState({
        address: '',
        price: 0,
        year_built: 0,
        sqft: 0,
        beds: 0,
        bathrooms: 0,
        price_per_sqft: null,
        property_type: '',
        garage: 0,
        HOA_fees: 0,
        sqft_lot: 0,
    });
    const navigate = useNavigate();

    const calculatePricePerSqft = () => {
        const { price, sqft } = newListing;
        if (sqft !== 0) {
            return parseFloat(price) / parseFloat(sqft);
        }
        return null;
    };

    useEffect(() => {
        const calculatedPricePerSqft = calculatePricePerSqft();
        setNewListing((prevListing) => ({
            ...prevListing,
            price_per_sqft: calculatedPricePerSqft,
        }));
    }, [newListing.price, newListing.sqft, calculatePricePerSqft]);

    const handlePropertyTypeChange = (event) => {
        const selectedPropertyType = event.target.value;
        setNewListing((prevListing) => ({
            ...prevListing,
            property_type: prevListing.property_type === selectedPropertyType ? '' : selectedPropertyType,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        for (const key in newListing) {
            if (!newListing[key]) {
                if (key === 'price_per_sqft') {
                    continue;
                }
                alert(`Please fill in the ${key} field.`);
                return;
            }
        }
        try {
            const response = await axios.post('http://localhost:8000/add-listing', newListing, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.status === 200) {
                navigate("/listings");
            } else {
                console.error('Error:', response.status, response.statusText);
                alert('Error adding listing. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const renderInputLabel = (label) => (
        <InputLabel>{label}</InputLabel>
    );

    return (
        <Container>
            <Typography variant="h4" align="center" style={{ marginBottom: '16px' }}>
                New Listing
            </Typography>
            <form onSubmit={handleSubmit}>
                <Grid container spacing={2}>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Address')}
                        <TextField
                            fullWidth
                            value={newListing.address}
                            onChange={(e) => setNewListing({ ...newListing, address: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Property Type')}
                        <Select
                            fullWidth
                            value={newListing.property_type}
                            onChange={handlePropertyTypeChange}>
                            <MenuItem value="Single family">Single family</MenuItem>
                            <MenuItem value="Condo">Condo</MenuItem>
                            <MenuItem value="Townhome">Townhome</MenuItem>
                            <MenuItem value="Multi-Family">Multi-Family</MenuItem>
                        </Select>
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Year Built')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.year_built}
                            onChange={(e) => setNewListing({ ...newListing, year_built: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Square Footage')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.sqft}
                            onChange={(e) => setNewListing({ ...newListing, sqft: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Bedrooms')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.beds}
                            onChange={(e) => setNewListing({ ...newListing, beds: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Bathrooms')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.bathrooms}
                            onChange={(e) => setNewListing({ ...newListing, bathrooms: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Price')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.price}
                            onChange={(e) => setNewListing({ ...newListing, price: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Garage')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.garage}
                            onChange={(e) => setNewListing({ ...newListing, garage: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('HOA Fees')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.HOA_fees}
                            onChange={(e) => setNewListing({ ...newListing, HOA_fees: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        {renderInputLabel('Sqft Lot')}
                        <TextField
                            fullWidth
                            type="number"
                            value={newListing.sqft_lot}
                            onChange={(e) => setNewListing({ ...newListing, sqft_lot: e.target.value })}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <Button type="submit" variant="contained" color="primary">
                            Add Listing
                        </Button>
                    </Grid>
                </Grid>
            </form>
        </Container>
    );
};

export default NewListingForm;
