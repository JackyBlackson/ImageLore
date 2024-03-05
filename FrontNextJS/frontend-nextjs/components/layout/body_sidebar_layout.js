'use client'

const BodySidebarLayout = ({ body, sidebar }) => {
  return (
    <main>
      <div id="basic-container" className="container-fluid">
        <div id="body-container" className="row m-3 il-round-border" style={{'height':'100%'}}>

          <div id="content-container" className="col-xl-8">
            <div id="content" className="il-item">
              {body}
            </div>
          </div>

          <div id="sidebar-container" className="col-xl-4">
            <div id="sidebar-test" className="il-item">
              {sidebar}
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default BodySidebarLayout;