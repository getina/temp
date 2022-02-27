
chrome.runtime.onInstalled.addListener( () => {
  chrome.contextMenus.create({
    id: 'textBox',
    title: "textbox: %s", 
    contexts:[ "selection" ]
  });
});

chrome.contextMenus.onClicked.addListener( ( info, tab ) => {
  if ( 'textBox' === info.menuItemId ) {
    notify( info.selectionText );
  }
} );