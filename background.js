chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ hello: "world" });
});
