import { useState, useRef } from "react"
import { NavLink } from "react-router-dom"
import { Nav, Logo, Menu, MenuItem, StyledNavLink, Search, Dropdown, DropdownMenu, DropdownItem } from "@/styles/navigation_styled"
import * as ROUTES from '@/constants/routes.js'

const Navigation = () => {
    const navbar = useRef(null)


    return (
        <Nav>
        <Logo>
          LOGO
        </Logo>
        <Menu>
          <MenuItem>
            <StyledNavLink to={ROUTES.MEN}>Men</StyledNavLink>
          </MenuItem>
          <MenuItem>
            <StyledNavLink to={ROUTES.WOMEN}>Women</StyledNavLink>
          </MenuItem>
        </Menu>
  
        <Search>
          search
        </Search>
  
        <Menu>
          <MenuItem>
            USER ICON
            <Dropdown>
              <DropdownMenu>
                <DropdownItem>
                  <StyledNavLink to={ROUTES.ACCOUNT}>My account</StyledNavLink>
                </DropdownItem>
                <DropdownItem>
                  <StyledNavLink to={ROUTES.ORDERHISTORY}>My orders</StyledNavLink>
                </DropdownItem>
              </DropdownMenu>
            </Dropdown>
          </MenuItem>
          <MenuItem>
            <StyledNavLink to={ROUTES.LIKEPRODUCT}>LIKE PRODUCT ICON</StyledNavLink>
          </MenuItem>
          <MenuItem>
            <StyledNavLink to={ROUTES.CAR}>CAR ICON</StyledNavLink>
          </MenuItem>
        </Menu>
      </Nav>
    )
}

export default Navigation