import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './src/pages/Home'
import About from './src/pages/about'
import Contact from './src/pages/contact'
import Education from './src/pages/education'
import Project from './src/pages/project'
import Layout from './components/Layout'
import Counter from './src/pages/counter'
import Services from './src/pages/services'
const MainRouter = () => {
return (<div>
<Layout/>
<Routes>
<Route exact path="/" element={<Home />} />
<Route exact path="/about" element={<About />} />
<Route exact path="/education" element={<Education />} />
<Route exact path="/project" element={<Project />} />
<Route exact path="/contact" element={<Contact />} />
<Route exact path="/counter" element={<Counter />} />
<Route exact path="/services" element={<Services />} />
</Routes>
</div>
)
}
export default MainRouter