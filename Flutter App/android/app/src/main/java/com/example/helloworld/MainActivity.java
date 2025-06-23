package com.example.helloworld;

import android.os.Bundle;
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodChannel;

public class MainActivity extends FlutterActivity {
    private static final String CHANNEL = "smartcommute/route";

    @Override
    public void configureFlutterEngine(FlutterEngine flutterEngine) {
        super.configureFlutterEngine(flutterEngine);

        new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), CHANNEL)
            .setMethodCallHandler((call, result) -> {
                if (call.method.equals("computeRoute")) {
                    String source = call.argument("source");
                    String destination = call.argument("destination");

                    String route = RouteLoader.computeRoute(source, destination);
                    result.success(route);
                } else {
                    result.notImplemented();
                }
            });
    }
}
