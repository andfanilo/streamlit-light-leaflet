import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)


def my_component(key=None):
    component_value = _component_func(key=key, default=0)
    return component_value


if not _RELEASE:
    import streamlit as st
    st.subheader("Leaflet - return coords on click")
    clicked_coords = my_component()
    st.markdown(clicked_coords)
