plugins {
    id("java")
    id("org.jetbrains.intellij.platform") version "2.19.0"
}

group = "com.devnamrits"
version = "0.1.0"

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

dependencies {
    intellijPlatform {
        val localIde = providers.gradleProperty("localIdePath").orNull
        if (localIde != null) {
            local(localIde)
        } else {
            intellijIdeaCommunity("2026.2.1")
        }
    }
}

intellijPlatform {
    buildSearchableOptions = false

    pluginConfiguration {
        id = "com.devnamrits.gruvboxarchipelago"
        name = "Gruvbox Archipelago"
        version = project.version.toString()

        ideaVersion {
            sinceBuild = "253"
            untilBuild = "262.*"
        }

        vendor {
            name = "devnamrits"
            url = "https://github.com/devnamrits/gruvbox-archipelago"
        }
    }
}
