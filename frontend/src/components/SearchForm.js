import React, { useState } from 'react';
import { Container, Grid, Typography, TextField, Checkbox, InputLabel, Select, MenuItem, Button, FormGroup, FormControlLabel, } from '@mui/material';
import ListingGrid from './ListingGrid';
import axios from 'axios';

const UserPreferencesForm = () => {
    const [searchCriteria, setSearchCriteria] = useState({
        min_price: 0,
        max_price: 0,
        min_year_built: 0,
        min_sqft: 0,
        max_sqft: 0,
        min_beds: 0,
        max_beds: 0,
        min_bathrooms: 0,
        max_bathrooms: 0,
        min_price_per_sqft: 0,
        property_type: [],
        min_garage: 0,
        max_HOA_fees: 0,
        address: '',
        min_sqft_lot: 0,
    });
    const [listingsData, setListings] = useState(null);
    const [noListings, setNoListings] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/search', searchCriteria, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            console.log("this is no listings", noListings);

            if (!response.data || response.data === 0) {
                setNoListings(true);
                console.log("this is no listings", noListings);
            } else {
                setNoListings(false);

                console.log("this is no listings", noListings);
            }


            setListings(response.data);
        } catch (error) {
            setNoListings(true);

            setListings(null);
            console.error('Error:', error);
        }
    };

    const handlePropertyTypeChange = (event) => {
        const selectedPropertyType = event.target.value;
        setSearchCriteria((prevSearchCriteria) => ({
            ...prevSearchCriteria,
            property_type: prevSearchCriteria.property_type.includes(selectedPropertyType)
                ? prevSearchCriteria.property_type.filter((type) => type !== selectedPropertyType)
                : [...prevSearchCriteria.property_type, selectedPropertyType],
        }));
    };

    return (
        <Container>
            <Typography variant="h4" align="center" mt={4}>
                User Preferences
            </Typography>
            <form onSubmit={handleSubmit}>
                <Grid container spacing={2}>
                    <Grid item xs={12} md={12} lg={12} xl={4}>
                        <TextField label="Location" fullWidth value={searchCriteria.address} onChange={(e) => setSearchCriteria({ ...searchCriteria, address: e.target.value })} />
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Property Type</InputLabel>
                        <FormGroup>
                            <Grid container>
                                <Grid item xs={3}>
                                    <FormControlLabel
                                        control={<Checkbox checked={searchCriteria.property_type.includes('Single family')} onChange={handlePropertyTypeChange} value='Single family' />}
                                        label="Single family"
                                    />
                                </Grid>
                                <Grid item xs={3}>
                                    <FormControlLabel
                                        control={<Checkbox checked={searchCriteria.property_type.includes('condo')} onChange={handlePropertyTypeChange} value='condo' />}
                                        label="condo"
                                    />
                                </Grid>
                                <Grid item xs={3}>
                                    <FormControlLabel
                                        control={<Checkbox checked={searchCriteria.property_type.includes('Townhome')} onChange={handlePropertyTypeChange} value='Townhome' />}
                                        label="Townhome"
                                    />
                                </Grid>
                                <Grid item xs={3}>
                                    <FormControlLabel
                                        control={<Checkbox checked={searchCriteria.property_type.includes('Multi-Family')} onChange={handlePropertyTypeChange} value='Multi-Family' />}
                                        label="Multi-Family"
                                    />
                                </Grid>
                            </Grid>
                        </FormGroup>
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Price Range</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_price} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_price: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={50000}>50,000</MenuItem>
                                    <MenuItem value={100000}>100,000</MenuItem>
                                    <MenuItem value={1500000}>150,000</MenuItem>
                                    <MenuItem value={2000000}>200,000</MenuItem>
                                </Select>
                            </Grid>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_price} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_price: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={50000}>50,000</MenuItem>
                                    <MenuItem value={100000}>100,000</MenuItem>
                                    <MenuItem value={1500000}>150,000</MenuItem>
                                    <MenuItem value={2000000}>200,000</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>


                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Bedrooms Range</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_beds} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_beds: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1}>1</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={3}>3</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                </Select>
                            </Grid>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_beds} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_beds: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1}>1</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={3}>3</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Bathrooms Range</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_bathrooms} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_bathrooms: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1}>1</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={3}>3</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                </Select>
                            </Grid>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_bathrooms} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_bathrooms: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1}>1</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={3}>3</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Max HOA Fees</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_HOA_fees} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_HOA_fees: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={100}>100</MenuItem>
                                    <MenuItem value={200}>200</MenuItem>
                                    <MenuItem value={300}>300</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Sqft Range</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_sqft} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_sqft: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={500}>500 sqft</MenuItem>
                                    <MenuItem value={1000}>1,000 sqft</MenuItem>
                                    <MenuItem value={1500}>1,500 sqft</MenuItem>
                                </Select>
                            </Grid>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_sqft} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_sqft: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1000}>1,000 sqft</MenuItem>
                                    <MenuItem value={1500}>1,500 sqft</MenuItem>
                                    <MenuItem value={2000}>2,000 sqft</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Sqft Lot Range</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_sqft_lot} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_sqft_lot: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={2000}>2,000 sqft</MenuItem>
                                    <MenuItem value={4000}>4,000 sqft</MenuItem>
                                    <MenuItem value={6000}>6,000 sqft</MenuItem>
                                </Select>
                            </Grid>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.max_sqft_lot} onChange={(e) => setSearchCriteria({ ...searchCriteria, max_sqft_lot: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={4000}>4,000 sqft</MenuItem>
                                    <MenuItem value={6000}>6,000 sqft</MenuItem>
                                    <MenuItem value={8000}>8,000 sqft</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} sm={6} md={6}>
                        <InputLabel>Min Built Year</InputLabel>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Select fullWidth value={searchCriteria.min_year_built} onChange={(e) => setSearchCriteria({ ...searchCriteria, min_year_built: e.target.value })}>
                                    <MenuItem value={0}>Any</MenuItem>
                                    <MenuItem value={1950}>1950</MenuItem>
                                    <MenuItem value={1980}>1980</MenuItem>
                                    <MenuItem value={2000}>2000</MenuItem>
                                    <MenuItem value={2010}>2010</MenuItem>
                                    <MenuItem value={2020}>2020</MenuItem>
                                </Select>
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid item xs={12}>
                        <Button type="submit" variant="contained" color="primary">
                            Save Preferences
                        </Button>
                    </Grid>
                </Grid>
            </form>

            {noListings ? (
                <Typography variant="body2" color="textSecondary" align="center">
                    No listings found for the specified criteria.
                </Typography>
            ) : null}

            {listingsData && listingsData.length !== 0 && <ListingGrid listings={listingsData} />}

        </Container>
    );
};

export default UserPreferencesForm;
