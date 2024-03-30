import React, { useContext } from 'react';
import { AppBar, Box, styled, Toolbar, Typography, Button } from "@mui/material";
import LocationCityIcon from '@mui/icons-material/LocationCity';
import { Link, useLocation } from 'react-router-dom';
import { AuthContext } from './AuthContext';
import { useNavigate } from 'react-router-dom';

const StyleToolbar = styled(Toolbar)({
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center"
});

const LeftLinks = styled("div")({
    display: "flex",
    alignItems: "center"
});

const RightLinks = styled("div")({
    display: "flex",
    alignItems: "center"
});

const Navbar = () => {
    const location = useLocation();
    const { isAuthenticated, logout } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate("/signin");
    };

    return (
        <AppBar position="static">
            <StyleToolbar>
                <LeftLinks>
                    <Typography variant="h6">
                        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                            <LocationCityIcon /> Listify
                        </Link>
                    </Typography>
                    <Box sx={{ display: 'flex', gap: '20px', alignItems: 'center', marginLeft: '20px' }}>
                        {isAuthenticated && (
                            <>
                                <Typography variant="h6">
                                    <Link to="/search" style={{ textDecoration: 'none', color: location.pathname === '/search' ? 'primary' : 'inherit' }}>
                                        Search
                                    </Link>
                                </Typography>

                                <Typography variant="h6">
                                    <Link to="/listings" style={{ textDecoration: 'none', color: location.pathname === '/listings' ? 'primary' : 'inherit' }}>
                                        Listings
                                    </Link>
                                </Typography>

                                <Typography variant="h6">
                                    <Link to="/addnew" style={{ textDecoration: 'none', color: location.pathname === '/addnew' ? 'primary' : 'inherit' }}>
                                        Add New
                                    </Link>
                                </Typography>
                            </>
                        )}
                    </Box>
                </LeftLinks>

                <RightLinks>
                    <Box sx={{ display: 'flex', gap: '20px', alignItems: 'center', marginLeft: '20px' }}>
                        {isAuthenticated ? (
                            <Typography variant="h6">
                                <Button variant="text" onClick={handleLogout} style={{ color: 'inherit' }}>
                                    Logout
                                </Button>
                            </Typography>
                        ) : (
                            <>
                                <Typography variant="h6">
                                    <Link to="/signin" style={{ textDecoration: 'none', color: 'inherit' }}>
                                        Sign In
                                    </Link>
                                </Typography>
                                <Typography variant="h6">
                                    <Link to="/signup" style={{ textDecoration: 'none', color: 'inherit' }}>
                                        Sign Up
                                    </Link>
                                </Typography>
                            </>
                        )}
                    </Box>
                </RightLinks>
            </StyleToolbar>
        </AppBar>
    );
}

export default Navbar;
