{
  description = "A very basic python dev flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = inputs: {
    devShells = builtins.mapAttrs (system: pkgs: {
      default = pkgs.mkShell {
        packages = with pkgs; [
          python315
        ];
        shellHook = ''
          echo "Welcome to the dev shell ig :P"
        '';
      };
    }) inputs.nixpkgs.legacyPackages;
  };
}
