import { AppBar, styled, Toolbar, Typography } from "@mui/material";
import LocationCityIcon from '@mui/icons-material/LocationCity';
import { Link } from 'react-router-dom'
import React from "react";

const StyleToolbar = styled(Toolbar)({
    display: "flex",
    justifyContent: "flex-start"
});

const LinkWrapper = styled("div")({
    marginLeft: "20px",
    display: "flex",
    gap: "20px",
});

const Navbar = () => {
    return (
        <AppBar position="static">
            <StyleToolbar>
                <Typography variant="h6" sx={{ display: { xs: "none", sm: "block" } }}>
                    <Link to="/">
                        <LocationCityIcon /> Listify
                    </Link>
                </Typography>

                <LinkWrapper>
                    <Typography variant="h6" sx={{ display: { xs: "none", sm: "block" } }}>
                        <Link to="/Search" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Search
                        </Link>
                    </Typography>

                    <Typography variant="h6" sx={{ display: { xs: "none", sm: "block" } }}>
                        <Link to="/listings" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Listings
                        </Link>
                    </Typography>

                    <Typography variant="h6" sx={{ display: { xs: "none", sm: "block" } }}>
                        <Link to="/addnew" style={{ textDecoration: 'none', color: 'inherit' }}>
                            AddNew
                        </Link>
                    </Typography>
                </LinkWrapper>
            </StyleToolbar>
        </AppBar>
    );
}

export default Navbar;
