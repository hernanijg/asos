import { NavLink } from 'react-router-dom'
import styled from 'styled-components'

const Nav = styled.nav`
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 1rm;
    color: white;
`

const Logo = styled.div`
    font-size: 1.5rem;
    color: white;
`

const Menu = styled.ul`
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
`

const MenuItem = styled.li`
    margin: 0 1rem;
    position: relative;

    &:hover > div {
        display: block;
    }
`

const StyledNavLink = styled(NavLink)`
    color: white;
    text-decoration: none;
    font-size: 1rem;

    &:hover {
        color: #ddd;
    }

    &:active {
        font-weight: bold;
        border-bottom: 2px solid white;
    }
`

const Search = styled.div`
    color: white;
`

const Dropdown = styled.div`
    display: None;
    position: absolute;
    background-color: #333;
    top: 100%;
    left: 0;
    min-width: 150px;
    z-index: 1;
`

const DropdownMenu = styled.ul`
    list-style: none;
    padding: 0;
    margin: 0;
`

const DropdownItem = styled.li`
    padding: 0.5rem 1rem;

    &:hover {
        background-color: #444;
    }
`

export { Nav, Logo, Menu, MenuItem, StyledNavLink, Search, Dropdown, DropdownMenu, DropdownItem }