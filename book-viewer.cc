#pragma comment( linker, "/subsystem:\"windows\" /entry:\"mainCRTStartup\"" )
#include "webview.h"
#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <filesystem>
#include "json.hpp"
using namespace std;
using json = nlohmann::json;

RECT rect;
bool maximized = true;

bool IsWindowMaximized(HWND hwnd) {
	WINDOWPLACEMENT placement;
	placement.length = sizeof(WINDOWPLACEMENT);
	if (GetWindowPlacement(hwnd, &placement)) {
		return placement.showCmd == SW_MAXIMIZE;
	}
	return false;
}

void SetFullscreen(HWND hWnd) {
	maximized = IsWindowMaximized(hWnd);
	if(maximized) ShowWindow(hWnd, SW_SHOWNORMAL);
	GetWindowRect(hWnd, &rect);
	SetWindowLong(hWnd, GWL_STYLE, WS_POPUP | WS_VISIBLE);
	SetWindowPos(hWnd, HWND_TOP, 0, 0, GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN), SWP_SHOWWINDOW);
}

void RestoreWindow(HWND hWnd) {
	SetWindowLong(hWnd, GWL_STYLE, WS_OVERLAPPEDWINDOW);
	SetWindowPos(hWnd, NULL, rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top, SWP_SHOWWINDOW);
	if (maximized)ShowWindow(hWnd, SW_SHOWMAXIMIZED);
}

int main(int argc, char ** argv) {

	webview::webview w = webview::webview(1, NULL);
	w.set_title("book-viewer");
	
	filesystem::path p(argv[0]);

	ifstream html(p.parent_path() / "index.html");
	stringstream htmlbuffer;
	htmlbuffer << html.rdbuf();
	html.close();

	w.bind("SetFullscreen", [&](const std::string& req) -> std::string {
		SetFullscreen((HWND)w.window());
		return "null";
	});

	w.bind("RestoreWindow", [&](const std::string& req) -> std::string {
		RestoreWindow((HWND)w.window());
		return "null";
	});
	static_cast<ICoreWebView2_3*>(w.m_webview)->SetVirtualHostNameToFolderMapping(L"book-viewer", L".", COREWEBVIEW2_HOST_RESOURCE_ACCESS_KIND_DENY_CORS);
	w.set_html(htmlbuffer.str());
	w.set_size(1920, 1080, WEBVIEW_HINT_NONE);

	if (argc != 2) {
		w.run();
		return 0;
	}

	json datatosend;
	datatosend["ext"] = filesystem::path(argv[1]).extension().string();

	if (datatosend["ext"] != ".json" && datatosend["ext"] != ".py") {
		w.run();
		return 0;
	}

	ifstream ifs(argv[1]);
	stringstream buffer;
	buffer << ifs.rdbuf();
	ifs.close();
	
	if (datatosend["ext"] == ".json") datatosend["data"] = json::parse(buffer.str());
	else datatosend["data"] = buffer.str();
	w.bind("datafunc", [&](const std::string& req) -> std::string {
		return datatosend.dump();
	});

	ShowWindow((HWND)w.window(), SW_SHOWMAXIMIZED);
	w.run();
	return 0;
}