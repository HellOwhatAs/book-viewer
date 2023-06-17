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

int main(int argc, char ** argv) {
	filesystem::path p(argv[0]);
	if (argc != 2) {
		cerr << "[Usage]: " << p.filename().string() << " <path to json/py>";
		return 1;
	}

	json datatosend;
	datatosend["ext"] = filesystem::path(argv[1]).extension().string();

	if (datatosend["ext"] != ".json" && datatosend["ext"] != ".py") {
		cerr << "[Usage]: " << p.filename().string() << " <path to json/py>";
		return 1;
	}

	ifstream ifs(argv[1]);
	stringstream buffer;
	buffer << ifs.rdbuf();
	ifs.close();

	ifstream html(p.parent_path() / "index.html");
	stringstream htmlbuffer;
	htmlbuffer << html.rdbuf();
	html.close();

	webview::webview w = webview::webview(1, NULL);
	w.set_title("book-viewer");
	
	if (datatosend["ext"] == ".json") datatosend["data"] = json::parse(buffer.str());
	else datatosend["data"] = buffer.str();
	w.bind("datafunc", [&](const std::string& req) -> std::string {
		return datatosend.dump();
	});

	w.set_html(htmlbuffer.str());
	w.set_size(1920, 1080, WEBVIEW_HINT_NONE);
	ShowWindow((HWND)w.window(), SW_SHOWMAXIMIZED);
	w.run();
	return 0;
}