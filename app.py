# app.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Containerization vs. Virtualization")

# --- Data for components (simplified descriptions for Streamlit) ---
virtualization_data = {
    'physical-server': {
        'name': 'Physical Server',
        'description': 'The underlying physical hardware (CPU, RAM, storage).',
        'color': 'bg-blue-100 border-blue-300'
    },
    'hypervisor': {
        'name': 'Hypervisor',
        'description': 'Software that creates and runs virtual machines (VMs). It manages hardware resources for VMs.',
        'color': 'bg-purple-100 border-purple-300'
    },
    'vm': {
        'name': 'Virtual Machine (VM)',
        'description': 'An isolated environment with its own OS, libraries, and application, simulating a complete computer system.',
        'color': 'bg-green-100 border-green-300'
    },
    'guest-os': {
        'name': 'Guest OS',
        'description': 'The operating system (e.g., Windows, Linux) running inside a virtual machine.',
        'color': 'bg-red-100 border-red-300'
    },
    'libs-bins-vm': {
        'name': 'Libraries & Binaries (VM)',
        'description': 'Software dependencies and executable files within the VM.',
        'color': 'bg-yellow-100 border-yellow-300'
    },
    'app-vm': {
        'name': 'Application (VM)',
        'description': 'The software application running on the Guest OS within the VM.',
        'color': 'bg-indigo-100 border-indigo-300'
    }
}

containerization_data = {
    'physical-server-cont': {
        'name': 'Physical Server',
        'description': 'The underlying physical hardware.',
        'color': 'bg-blue-100 border-blue-300'
    },
    'host-os': {
        'name': 'Host OS',
        'description': 'The operating system installed directly on the physical server. Containers share its kernel.',
        'color': 'bg-orange-100 border-orange-300'
    },
    'container-runtime': {
        'name': 'Container Runtime',
        'description': 'Software (like Docker Engine) that manages containers, creating and running them.',
        'color': 'bg-teal-100 border-teal-300'
    },
    'container': {
        'name': 'Container',
        'description': 'A lightweight, portable package that bundles an application and its dependencies, sharing the host OS kernel.',
        'color': 'bg-pink-100 border-pink-300'
    },
    'libs-bins-cont': {
        'name': 'Libraries & Binaries (Container)',
        'description': 'Software dependencies and executable files within the container.',
        'color': 'bg-yellow-100 border-yellow-300'
    },
    'app-cont': {
        'name': 'Application (Container)',
        'description': 'The software application running inside the container.',
        'color': 'bg-indigo-100 border-indigo-300'
    }
}

# --- Utility for component HTML (simplified styling for demonstration) ---
def get_component_html(comp_id, data_dict, level_indent=0):
    comp = data_dict[comp_id]
    margin_left = level_indent * 20 # Adjust as needed for nesting visual
    html = f"""
    <div style="
        border: 2px solid var(--{comp_id}-border-color, #ccc);
        background-color: var(--{comp_id}-bg-color, #f0f0f0);
        padding: 10px; margin-bottom: 5px; border-radius: 8px;
        margin-left: {margin_left}px;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        "
        onmouseover="this.style.boxShadow='0 4px 8px rgba(0,0,0,0.1)';"
        onmouseout="this.style.boxShadow='none';"
        onclick="parent.postMessage('{{ "source": "streamlit", "type": "click", "id": "{comp_id}" }}', '*');"
        >
        <b>{comp['name']}</b>
    </div>
    """
    return html

# --- Main Streamlit App ---
st.title("Containerization vs. Virtualization Visualizer")

# Tabs
tab_virtualization, tab_containerization = st.tabs(["Virtualization", "Containerization"])

with tab_virtualization:
    st.header("Virtualization Architecture")
    st.markdown("Click on any component to see its description below.", unsafe_allow_html=True)

    # Simplified Visualization Structure using Streamlit columns and markdown
    # (More complex styling would require more detailed custom CSS)

    st.markdown(f"""
    <style>
        .stTabs [data-baseweb="tab-list"] button {{
            font-size: 16px;
            padding: 10px 20px;
        }}
        .component-box {{
            border: 2px solid #ccc;
            padding: 10px;
            margin-bottom: 5px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }}
        .component-box:hover {{
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .physical-server {{ border-color: #90CAF9; background-color: #E3F2FD; }}
        .hypervisor {{ border-color: #BBDEFB; background-color: #E0F2F7; }}
        .vm {{ border-color: #C8E6C9; background-color: #E8F5E9; }}
        .guest-os {{ border-color: #EF9A9A; background-color: #FFEBEE; }}
        .libs-bins-vm {{ border-color: #FFEB3B; background-color: #FFFDE7; }}
        .app-vm {{ border-color: #C5CAE9; background-color: #E8EAF6; }}

        .host-os {{ border-color: #FFCC80; background-color: #FFF3E0; }}
        .container-runtime {{ border-color: #B2DFDB; background-color: #E0F7FA; }}
        .container {{ border-color: #F8BBD0; background-color: #FCE4EC; }}
        .libs-bins-cont {{ border-color: #FFEB3B; background-color: #FFFDE7; }}
        .app-cont {{ border-color: #C5CAE9; background-color: #E8EAF6; }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="component-box physical-server" id="physical-server">
            <b>Physical Server</b>
            <div style="margin-left: 20px;">
                <div class="component-box hypervisor" id="hypervisor">
                    <b>Hypervisor</b>
                    <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                        <div class="component-box vm" id="vm-1" style="width: 48%;">
                            <b>VM 1</b>
                            <div style="margin-left: 10px;">
                                <div class="component-box guest-os" id="guest-os">Guest OS</div>
                                <div class="component-box libs-bins-vm" id="libs-bins-vm">Libs & Bins</div>
                                <div class="component-box app-vm" id="app-vm">Application</div>
                            </div>
                        </div>
                        <div class="component-box vm" id="vm-2" style="width: 48%;">
                            <b>VM 2</b>
                            <div style="margin-left: 10px;">
                                <div class="component-box guest-os" id="guest-os">Guest OS</div>
                                <div class="component-box libs-bins-vm" id="libs-bins-vm">Libs & Bins</div>
                                <div class="component-box app-vm" id="app-vm">Application</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


with tab_containerization:
    st.header("Containerization Architecture")
    st.markdown("Click on any component to see its description below.", unsafe_allow_html=True)

    st.markdown("""
        <div class="component-box physical-server" id="physical-server-cont">
            <b>Physical Server</b>
            <div style="margin-left: 20px;">
                <div class="component-box host-os" id="host-os">
                    <b>Host OS</b>
                    <div style="margin-left: 20px;">
                        <div class="component-box container-runtime" id="container-runtime">
                            <b>Container Runtime</b>
                            <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                                <div class="component-box container" id="container-1" style="width: 30%;">
                                    <b>Container 1</b>
                                    <div style="margin-left: 5px; font-size: 0.9em;">
                                        <div class="component-box libs-bins-cont" id="libs-bins-cont">Libs & Bins</div>
                                        <div class="component-box app-cont" id="app-cont">Application</div>
                                    </div>
                                </div>
                                <div class="component-box container" id="container-2" style="width: 30%;">
                                    <b>Container 2</b>
                                    <div style="margin-left: 5px; font-size: 0.9em;">
                                        <div class="component-box libs-bins-cont" id="libs-bins-cont">Libs & Bins</div>
                                        <div class="component-box app-cont" id="app-cont">Application</div>
                                    </div>
                                </div>
                                <div class="component-box container" id="container-3" style="width: 30%;">
                                    <b>Container 3</b>
                                    <div style="margin-left: 5px; font-size: 0.9em;">
                                        <div class="component-box libs-bins-cont" id="libs-bins-cont">Libs & Bins</div>
                                        <div class="component-box app-cont" id="app-cont">Application</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- Component Details Display ---
st.subheader("Component Details:")
if 'selected_component' not in st.session_state:
    st.session_state.selected_component = None

# Custom HTML for click events to communicate with Streamlit
# We use st.components.v1.html for this.
# This injects JavaScript that sends messages back to Streamlit when a box is clicked.
js_code = """
<script>
    const setupClickListeners = () => {
        document.querySelectorAll('.component-box').forEach(box => {
            box.onclick = (event) => {
                event.stopPropagation(); // Prevent bubbling up
                const componentId = event.currentTarget.id;
                // Send a message back to Streamlit
                window.parent.postMessage({
                    type: 'streamlit:component_event',
                    args: {
                        id: componentId,
                        message: 'clicked'
                    }
                }, '*');
            };
        });
    };

    // Re-run setupClickListeners on every render to ensure listeners are re-attached
    setupClickListeners();

    // Observe changes to the DOM and re-attach listeners if new elements are added
    const observer = new MutationObserver(setupClickListeners);
    observer.observe(document.body, { childList: true, subtree: true });

    // Initial setup
    setupClickListeners();
</script>
"""
components.html(js_code, height=0, width=0) # height and width 0 as it's just for injecting JS

# --- Handle messages from the embedded HTML/JS ---
# This part is a bit tricky with Streamlit's refresh model.
# A simpler way for demos is to use `st.session_state` with button clicks.
# For interactive clicks on custom HTML, you generally need a custom component.
# The above JS with `postMessage` is a simplified attempt to trigger a re-render.

# For direct HTML elements, Streamlit doesn't automatically detect clicks on them.
# A more common Streamlit approach is to use Streamlit's own buttons/expander.
# Let's add a basic way to show details based on a placeholder selection for demonstration.

# For a more reliable "click" interaction with purely HTML elements:
# You'd typically need a custom Streamlit component (React component)
# that passes events to Python.
# For this example, I'll demonstrate with Streamlit buttons for simplicity of interaction.

st.write("---")
st.subheader("Explanation of Components:")

# Use Streamlit buttons or expanders to select components for explanation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Physical Server (All)"):
        st.session_state.selected_component = virtualization_data['physical-server']
    if st.button("Hypervisor"):
        st.session_state.selected_component = virtualization_data['hypervisor']
    if st.button("Virtual Machine (VM)"):
        st.session_state.selected_component = virtualization_data['vm']
with col2:
    if st.button("Host OS"):
        st.session_state.selected_component = containerization_data['host-os']
    if st.button("Container Runtime"):
        st.session_state.selected_component = containerization_data['container-runtime']
    if st.button("Container"):
        st.session_state.selected_component = containerization_data['container']
with col3:
    if st.button("Guest OS"):
        st.session_state.selected_component = virtualization_data['guest-os']
    if st.button("Libs & Bins"):
        st.session_state.selected_component = virtualization_data['libs-bins-vm'] # Using VM one as generic
    if st.button("Application"):
        st.session_state.selected_component = virtualization_data['app-vm'] # Using VM one as generic

if st.session_state.selected_component:
    st.markdown(f"""
        <div style="
            border: 1px solid #ddd;
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        ">
            <h4>{st.session_state.selected_component['name']}</h4>
            <p>{st.session_state.selected_component['description']}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Click a button above to see details about a component.")


# --- General Information ---
st.write("---")
st.header("Key Differences & Benefits")

col_virt, col_cont = st.columns(2)

with col_virt:
    st.subheader("Virtualization")
    st.markdown("""
    - Each VM has its own **full operating system**.
    - Provides **strong isolation** between VMs.
    - **Higher resource overhead** due to multiple OS instances.
    - Slower to provision and boot up.
    - Ideal for running different operating systems on a single physical server.
    """)

with col_cont:
    st.subheader("Containerization")
    st.markdown("""
    - Containers **share the host OS kernel**.
    - **Lighter weight** and faster to start.
    - **Lower resource overhead** as there's only one OS kernel.
    - Provides process-level isolation, not full OS isolation.
    - Excellent for microservices and continuous integration/delivery (CI/CD).
    """)

st.markdown("""
<p class="text-center text-gray-600 mt-8 text-sm md:text-base">
    Both technologies aim to maximize hardware utilization and improve deployment efficiency, but they achieve this through different architectural approaches.
</p>
""", unsafe_allow_html=True)
